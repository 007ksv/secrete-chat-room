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

sock.bind(("127.0.0.1", 9999))

sock.listen(5)

(client , (ip, port)) = sock.accept()

print("server got connection from : ", ip , "   ", port )

while True:
	data = "KSV>>"+ input("type here>>")
	client.send(data.encode())
	print(client.recv(1024))