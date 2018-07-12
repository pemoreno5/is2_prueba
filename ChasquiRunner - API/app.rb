require 'sinatra'
require_relative 'config/database'

get '/jugador/listar' do
  return DB[:jugador].all.to_a.to_json
end

get '/jugador/:id' do
  rpta = DB[:jugador].where(id: params[:id]).first.to_json
  if rpta == 'null'
    rpta = 'Jugador no existe'
  else
    return rpta
  end
end

get '/jugador/status/:status' do
  rpta = DB[:jugador].where(status: params[:status]).first.to_json
  if rpta == 'null'
    rpta = 'Jugador no existe'
  else
    return rpta
  end
end

delete '/jugador/eliminar' do
  peticion = JSON.parse(request.body.read)
  usuario = peticion['usuario']
  puts usuario
  rpta = DB[:jugador].where(usuario: usuario).delete
  if rpta == 'null'
    rpta = 'Jugador no existe'
  else
    redirect '/jugador/listar'
    
  end
end

post '/jugador/crear' do
  peticion = JSON.parse(request.body.read)
  puts peticion
  usuario = peticion['usuario']
  status = peticion['status']
  tags = peticion['tags']
  score = peticion['score']
  puts peticion['usuario']
  puts status
  DB[:jugador].insert(usuario: usuario, status: status, tags: tags, score: score)
  redirect 'jugador/listar'
end

delete '/eliminarescenario/:id' do
  rpta = DB[:escenario].where(id: params[:id]).delete
  if rpta == 'null'
    rpta = 'Escenario no existe'
  end
end

get '/escenario/listar' do
  return DB[:escenario].all.to_a.to_json
end

get '/jugador/listar' do
  return DB[:escenario].all.to_a.to_json
end

post '/escenario/crear' do
  id = params['id']
  nombre = params['nombre']
  repositorio = params['repositorio']
  DB[:sistemas].insert(id: id, nombre: nombre, repositorio: repositorio)
  redirect 'escenario/listar'
end

get '/obstaculo/listar' do
  return DB[:obstaculo].all.to_a.to_json
end

get '/obstaculo/:id' do
  rpta = DB[:obstaculo].where(id: params[:id]).first.to_json
  if rpta == 'null'
    rpta = 'Obstaculo no existe'
  end
end

get '/obstaculo/:nombre' do
  rpta = DB[:obstaculo].where(nombre: params[:nombre]).first.to_json
  if rpta == 'null'
    rpta = 'Obstaculo no existe'
  end
end

post '/obstaculo/crear' do
  id = params['id']
  nombre = params['nombre']
  DB[:sistemas].insert(id: id, nombre: nombre)
  redirect 'obstaculo/listar'
end

delete '/eliminarobstaculo/:id' do
  rpta = DB[:escenario].where(id: params[:id]).delete
  if rpta == 'null'
    rpta = 'Obstaculo no existe'
  end
end

get '/powerups/listar' do
  return DB[:powerups].all.to_a.to_json
end

get '/powerups/:id' do
  rpta = DB[:powerups].where(id: params[:id]).first.to_json
  if rpta == 'null'
    rpta = 'Powerup no existe'
  end
end

get '/powerups/:nombre' do
  rpta = DB[:powerups].where(nombre: params[:nombre]).first.to_json
  if rpta == 'null'
    rpta = 'Powerups no existe'
  end
end

post '/powerups/crear' do
  id = params['id']
  nombre = params['nombre']
  DB[:sistemas].insert(id: id, nombre: nombre)
  redirect 'powerups/listar'
end

delete '/eliminarobstaculo/:id' do
  rpta = DB[:powerups].where(id: params[:id]).delete
  if rpta == 'null'
    rpta = 'Powerups no existe'
  end
end
