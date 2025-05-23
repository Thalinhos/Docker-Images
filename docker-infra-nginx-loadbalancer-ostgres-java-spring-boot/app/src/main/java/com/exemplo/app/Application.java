package com.exemplo.app;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Application {

    @Autowired
    private UserRepository userRepository;

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
public CommandLineRunner createAdminUserIfNotExists() {
    return args -> {
        if (userRepository.findByUsername("admin").isEmpty()) {
            User admin = new User("admin", "admin");
            userRepository.save(admin);
            System.out.println("Admin user created.");
        }
    };
}

}
