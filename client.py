print('''                             SECRETE       CHAT         ROOM 
              ----------       ---           !\      !    !====\    !------    ----------   !       !
              !               /   \          ! \     !    !     \   !          !            !       !
              !              /     \         !  \    !    !      !  !          !            !       !
              !--------     / ----- \        !   \   !    !      !  !------    !--------!   !-------!
                       !   /         \       !    \  !    !      !  !                   !   !       !
                       !  /           \      !     \ !    !      !  !                   !   !       !
              ---------! /             \     !      \!    !=====/   !------    ---------!   !       ! 




     ''')

import socket

sock = socket.socket()

sock.connect(("127.0.0.1", 9999))

print("connected from server ")

while True:
	print(sock.recv(1024))
	data = "AK-47>>"+ input("type here>>")
	sock.send(data.encode())

