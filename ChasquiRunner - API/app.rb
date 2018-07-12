require 'sinatra'
require_relative 'config/database'

get '/jugador/listar' do
  return DB[:jugador].all.to_a.to_json
end

get '/jugador/id/:id' do
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

get '/escenario/listar' do
  return DB[:escenario].all.to_a.to_json
end

get '/escenario/id/:id' do
  rpta = DB[:escenario].where(id: params[:id]).first.to_json
  if rpta == 'null'
    rpta = 'Escenario no existe'
  else
    return rpta
  end
end

post '/escenario/crear' do
  peticion = JSON.parse(request.body.read)
  nombre = peticion['nombre']
  DB[:escenario].insert(nombre: nombre)
  redirect 'escenario/listar'
end

delete '/escenario/eliminar' do
  peticion = JSON.parse(request.body.read)
  nombre = peticion['nombre']
  puts escenario
  rpta = DB[:escenario].where(nombre: nombre).delete
  if rpta == 'null'
    rpta = 'Escenario no existe'
  else
    redirect '/escenario/listar'
  end
end

get '/obstaculo/listar' do
  return DB[:obstaculo].all.to_a.to_json
end

get '/obstaculo/id/:id' do
  rpta = DB[:obstaculo].where(id: params[:id]).first.to_json
  if rpta == 'null'
    rpta = 'Obstaculo no existe'
  else
    return rpta
  end
end

get '/obstaculo/:nombre' do
  rpta = DB[:obstaculo].where(nombre: params[:nombre]).first.to_json
  if rpta == 'null'
    rpta = 'Obstaculo no existe'
  end
end

post '/obstaculo/crear' do
  peticion = JSON.parse(request.body.read)
  nombre = peticion['nombre']
  DB[:obstaculo].insert(nombre: nombre)
  redirect 'obstaculo/listar'
end

delete '/obstaculo/eliminar' do
  peticion = JSON.parse(request.body.read)
  nombre = peticion['nombre']
  puts nombre
  rpta = DB[:obstaculo].where(nombre: nombre).delete
  if rpta == 'null'
    rpta = 'Obstaculo no existe'
  else
    redirect '/obstaculo/listar'
  end
end

get '/powerups/listar' do
  return DB[:powerups].all.to_a.to_json
end

get '/powerups/id/:id' do
  rpta = DB[:powerups].where(id: params[:id]).first.to_json
  if rpta == 'null'
    rpta = 'Powerup no existe'
  else
    return rpta
  end
end

get '/powerups/:nombre' do
  rpta = DB[:powerups].where(nombre: params[:nombre]).first.to_json
  if rpta == 'null'
    rpta = 'Powerups no existe'
  end
end

post '/powerups/crear' do
  peticion = JSON.parse(request.body.read)
  nombre = peticion['nombre']
  DB[:powerups].insert(nombre: nombre)
  redirect 'powerups/listar'
end

delete '/powerups/eliminar' do
  peticion = JSON.parse(request.body.read)
  nombre = peticion['nombre']
  puts nombre
  rpta = DB[:powerups].where(nombre: nombre).delete
  if rpta == 'null'
    rpta = 'Escenario no existe'
  else
    redirect '/powerups/listar'
  end
end