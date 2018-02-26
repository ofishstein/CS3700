Oliver Fishstein and Jacob Taylor
CS3700 - Networks and Distributed Systems
Project 3

High Level Approach
----
We decided to model features from TCP Reno such as sliding window, slow start, fast recovery, and packet timers. In order to do this we implemented a variety of features on the the Sender (3700send) and Receiver (3700recv) sides. 

#### Sender:

The sender is responsible for breaking the data up into packets and sending it to the receiver and for receiving acks and determing how to proceed. In order to do this we implemented the following methods in a Sender class:

* init 		                -> creates the object and initializes fields
* init_socket 	          -> creates a socket object to send and receive through
* send                    -> main send functionality that calls all other methods to send packets and receive acks
* transmit_eof            -> transmits the eof packet multiple times to ensure that it is received
* build_checksum          -> builds a checksum for the packet to ensure data validation on the receiver side
* calc_cong_wind_timeout  -> calculate the congestion window after socket timeout
* calc_cong_wind_dup_acks -> calculate the congestion window after 3 duplicate acks (fast recovery)
* calc_cong_wind_ack      -> calculate the congestion window after an ack (slow start)
* transmit_packet         -> creates and sends a single packet
* retransmit_packet       -> retransmits all packets for the sending window
* parse_receiver_msg      -> parse the json for ack
* process_ack             -> process the acks and deligates to other methods for dup acks when neccessary
* handle_dup_ack          -> handles receiving 3 duplicate acks by calling for congestion window recalculation and retransmitting the lost packet

#### Receiver:

The receiver is responsible for receiving packets and sending acknowledgements when valid data is received and printing the data in order. In order to do this we implemented the following methods in a Receiver class:

* init                -> creates the object and initializes fields
* init_socket         -> creates a socket object to send and receive through
* receive             -> main receive functionality 
* parse_sender_msg    -> parse the json for the packet
* process_packet      -> handles the info from the packet by buffering data, printing data, and sending acks
* build_checksum      -> builds a checksum from data received in the packet
* check_packet_valid  -> compares the sent checksum and the checksum built from received data to check if its valid
* send_ack            -> sends an ack to the sender with the sequence for the packet received and the expected sequence number
* on_finished         -> handles ending program when eof is received

Challenges
----

We had challenges figuring out what TCP algorithms to implement at first, and then ran into issues optimizing our program for speed in order to pass tests within the timeouts especially for high data volume tests. As we implemented more TCP methods, though, our performance increased for the tests.   

Testing
----

In order to test, we ran the ./test script and also used ./run under different network configs with the --live flag in order to live debug and see what could be improved in each test run. 




