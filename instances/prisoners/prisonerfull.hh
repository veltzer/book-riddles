#ifndef __prisonerfull_hh
#define __prisonerfull_hh

#include "prisoner.hh"

class PrisonerFull:public Prisoner {
	private:
		bool* bits;
		unsigned int numBits;
		unsigned int mynum;
		unsigned int prisnum;
	public:
		PrisonerFull();
		~PrisonerFull();
		PrisonerFull(const PrisonerFull&)=delete;
		PrisonerFull& operator=(const PrisonerFull&)=delete;
		void init(int imynum,int iprisnum) override;
		void nullit(void) override;
		bool wantToEnd(void) override;
		bool doYourThing(bool light) override;
		void output(std::ostream& out) const override;

		void updateBit(unsigned int bit);
};

#endif // __prisonerfull_hh
