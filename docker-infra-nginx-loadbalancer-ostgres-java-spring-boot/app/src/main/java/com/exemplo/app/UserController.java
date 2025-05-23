package com.exemplo.app;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    @GetMapping
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    @GetMapping("/server")
    public String getServerIdentity() throws UnknownHostException {
        InetAddress inetAddress = InetAddress.getLocalHost();
        return "Server: " + inetAddress.getHostName() + " (" + inetAddress.getHostAddress() + ")";
    }
}
