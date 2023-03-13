class Employe {
    static String Emp_name, Emp_id, address, mail_id;
    static int m_num;
    double basicBay, gs, ns;

    Employe(String e, String e_id, String ad, String m_id, int mno) {
        Emp_name = e;
        Emp_id = e_id;
        address = ad;
        mail_id = m_id;
        m_num = mno;
    }

    double gross(double basicBay) {
        double DA = 0.97 * basicBay;
        double HRA = 0.1 * basicBay;
        gs = basicBay + DA + HRA;
        return gs;
    }

    double net() {
        double pf = 0.12 * basicBay;
        double s_c_fund = 0.001 * basicBay;
        ns = gs - pf - s_c_fund;
        return ns;
    }

    void display() {
        System.out.println("Name:" + Emp_name);
        System.out.println("Employee id:" + Emp_id);
        System.out.println("Address:" + address);
        System.out.println("Mail Id:" + mail_id);
        System.out.println("Mobile number:" + m_num);
    }
}

class Programmer extends Employe {
    Programmer() {
        super(Emp_id, Emp_id, Emp_id, Emp_id, m_num);z
    
	}
}

class AssistantProfesso extends Employe {
    AssistantProfesso() {
        super(Emp_id, Emp_id, Emp_id, Emp_id, m_num);
    }
    // double basicBay;
}

class AssociateProfesso extends Employe {
    AssociateProfesso(){
    	super(Emp_id, Emp_id, Emp_id, Emp_id, m_num)
    	
    }
}

class Professo extends Employe {
    Professo() {
        super(Emp_id, Emp_id, Emp_id, Emp_id, m_num);
    }
}
