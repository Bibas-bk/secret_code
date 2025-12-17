import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Calculator1 implements ActionListener {

    JFrame f1;
    JButton b1, b2, b3, b4;
    JTextField j1, j2, j3;
    JLabel t1, t2, t3;

    Calculator1() {
        f1 = new JFrame("***calculator***");
        f1.setSize(500, 500);
        f1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        GridBagLayout g1 = new GridBagLayout();
        f1.setLayout(g1);
        GridBagConstraints gbc = new GridBagConstraints();

        t1 = new JLabel("Num1");
        gbc.gridx = 0; gbc.gridy = 0;
        f1.add(t1, gbc);

        j1 = new JTextField(10);
        gbc.gridx = 1; gbc.gridy = 0;
        f1.add(j1, gbc);

        t2 = new JLabel("Num2");
        gbc.gridx = 0; gbc.gridy = 1;
        f1.add(t2, gbc);

        j2 = new JTextField(10);
        gbc.gridx = 1; gbc.gridy = 1;
        f1.add(j2, gbc);

        t3 = new JLabel("Result");
        gbc.gridx = 0; gbc.gridy = 2;
        f1.add(t3, gbc);

        j3 = new JTextField(10);
        j3.setEditable(false);
        gbc.gridx = 1; gbc.gridy = 2;
        f1.add(j3, gbc);

        b1 = new JButton("+");
        gbc.gridx = 0; gbc.gridy = 3;
        f1.add(b1, gbc);

        b2 = new JButton("-");
        gbc.gridx = 1; gbc.gridy = 3;
        f1.add(b2, gbc);

        b3 = new JButton("*");
        gbc.gridx = 0; gbc.gridy = 4;
        f1.add(b3, gbc);

        b4 = new JButton("/");
        gbc.gridx = 1; gbc.gridy = 4;
        f1.add(b4, gbc);

        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);

        f1.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        double n1 = Double.parseDouble(j1.getText());
        double n2 = Double.parseDouble(j2.getText());
        double result = 0;

        if (e.getSource() == b1) {
            result = n1 + n2;
        } else if (e.getSource() == b2) {
            result = n1 - n2;
        } else if (e.getSource() == b3) {
            result = n1 * n2;
        } else if (e.getSource() == b4) {
            result = n1 / n2;
        }

        j3.setText(String.valueOf(result));
    }

    public static void main(String[] args) {
        new Calculator1();
    }
}
