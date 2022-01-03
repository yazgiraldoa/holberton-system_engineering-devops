#Killing a process
exec {'killmenow':
  command  => 'pkill -15 killmenow',
  provider => 'shell',
}
