import React, { useState, useEffect, useRef } from "react";
import api from "./api"; 
import { Eye, EyeOff, User, Lock } from "lucide-react";

const App = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPass, setShowPass] = useState(false);
  const [status, setStatus] = useState("idle"); 
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const [currentTime, setCurrentTime] = useState(new Date());
  const eyeRef = useRef(null);

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    const handleMove = (e) => {
      if (eyeRef.current && !showPass) {
        const rect = eyeRef.current.getBoundingClientRect();
        const x = (e.clientX - (rect.left + rect.width / 2)) / 12;
        const y = (e.clientY - (rect.top + rect.height / 2)) / 12;
        setMousePos({ x, y });
      }
    };
    window.addEventListener("mousemove", handleMove);
    return () => {
      window.removeEventListener("mousemove", handleMove);
      clearInterval(timer);
    };
  }, [showPass]);

  const handleLogin = async (e) => {
    e.preventDefault();
    setStatus("loading");

    const formData = new URLSearchParams();
    formData.append("username", email); // <- OBLIGATORIO usar "username"
    formData.append("password", password);

    try {
      const response = await api.post("/auth/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      localStorage.setItem("token", response.data.access_token);
      setStatus("success");
    } catch (err) {
      setStatus("error");
      setTimeout(() => setStatus("idle"), 2000);
    }
  };

  const getStatusColor = () => {
    if (status === "success") return "#22c55e"; 
    if (status === "error") return "#ef4444";   
    return "#ffb400"; 
  };

  const statusColor = getStatusColor();

  return (
    <div className="stage-3d">
      <div 
        className="room" 
        style={{
          backgroundImage: `url('/fondo%20login.png')`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          position: 'absolute',
          inset: 0,
          zIndex: 1
        }}
      ></div>

      <div className="fixed top-6 right-8 text-[12px] text-cyan-400/60 font-mono tracking-[0.2em] z-50">
        {currentTime.toLocaleString('es-ES').toUpperCase()}
      </div>

      <div className={`relative z-10 w-full max-w-[420px] px-6 transition-transform ${status === 'error' ? 'animate-shake' : ''}`}>
        
        {/* SCANNER SUPERIOR */}
        <div className="relative w-48 h-48 mx-auto mb-[-85px] z-20 flex items-center justify-center">
          <div className="absolute inset-0 rounded-full border transition-colors duration-500" 
               style={{ borderColor: `${statusColor}33`, borderWidth: '1px' }}></div>
          
          <div ref={eyeRef} 
               className="w-20 h-20 bg-black rounded-full border-[3px] flex items-center justify-center overflow-hidden transition-all duration-500 shadow-lg"
               style={{ borderColor: statusColor }}>
            <div className="rounded-full transition-all duration-150"
                 style={{ 
                   backgroundColor: statusColor,
                   width: showPass ? '100%' : '20px',
                   height: showPass ? '2px' : '20px',
                   transform: showPass ? 'none' : `translate(${mousePos.x}px, ${mousePos.y}px)`,
                   boxShadow: `0 0 15px ${statusColor}`
                 }}></div>
          </div>
        </div>

        {/* CONTENEDOR LOGIN */}
        <div className="login-card bg-[#0a0a0a]/85 border p-10 pt-28 pb-14 rounded-[2.5rem] backdrop-blur-md relative transition-colors duration-500"
             style={{ borderColor: `${statusColor}66` }}>
          
          <div className="absolute left-0 top-1/2 -translate-y-1/2 w-[4px] h-32 transition-all duration-500" 
               style={{ backgroundColor: statusColor, boxShadow: `0 0 15px ${statusColor}` }}></div>
          <div className="absolute right-0 top-1/2 -translate-y-1/2 w-[4px] h-32 transition-all duration-500" 
               style={{ backgroundColor: statusColor, boxShadow: `0 0 15px ${statusColor}` }}></div>

          <div className="text-center mb-10">
            <h1 className="text-4xl font-black italic text-white tracking-tighter">
              SMART<span className="text-cyan-400">/METER</span>
            </h1>
          </div>

          <form onSubmit={handleLogin} className="space-y-5">
            <div className="relative">
              <User className="absolute left-4 top-1/2 -translate-y-1/2 text-cyan-500/50" size={16} />
              <input
                type="email"
                required
                className="w-full bg-black/40 border border-cyan-500/20 p-4 pl-12 rounded-xl focus:border-cyan-400 outline-none text-white font-mono text-sm"
                placeholder="OPERATOR_ID"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>

            <div className="relative">
              <Lock className="absolute left-4 top-1/2 -translate-y-1/2 text-cyan-500/50" size={16} />
              <input
                type={showPass ? "text" : "password"}
                required
                className="w-full bg-black/40 border border-cyan-500/20 p-4 pl-12 rounded-xl focus:border-cyan-400 outline-none text-white font-mono text-sm"
                placeholder="ACCESS_KEY"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <button type="button" onClick={() => setShowPass(!showPass)} className="absolute right-4 top-1/2 -translate-y-1/2 text-cyan-500/40 hover:text-cyan-400">
                {showPass ? <EyeOff size={16}/> : <Eye size={16}/>}
              </button>
            </div>

            <button
              type="submit"
              disabled={status === "loading"}
              className="w-full py-4 mt-4 text-black font-bold uppercase tracking-[0.2em] rounded-xl transition-all disabled:opacity-50"
              style={{ backgroundColor: statusColor, boxShadow: `0 5px 20px ${statusColor}4d` }}>
              {status === "loading" ? "SYNCING..." : "INITIALIZE"}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default App;