#include "prisonerfull.hh"

PrisonerFull::PrisonerFull():bits(nullptr),numBits(0),mynum(0),prisnum(0) {
}
PrisonerFull::~PrisonerFull() {
	delete[] bits;
}
void PrisonerFull::init(int imynum,int iprisnum) {
	mynum=imynum;
	prisnum=iprisnum;
	bits=new bool[prisnum];
}
void PrisonerFull::nullit(void) {
	numBits=0;
	for(unsigned int i=0;i<prisnum;i++) {
		bits[i]=false;
	}
	updateBit(mynum);
}
bool PrisonerFull::wantToEnd(void) {
	return numBits==prisnum;
}
bool PrisonerFull::doYourThing(bool light) {
	return light;
}
void PrisonerFull::output(std::ostream& out) const {
	out << "prisoner #" << mynum << " " << numBits << std::endl;
	for(unsigned int i=0;i<prisnum;i++) {
		out << bits[i];
	}
	out << std::endl;
}
void PrisonerFull::updateBit(unsigned int bit) {
	if(bits[bit]==false) {
		bits[bit]=true;
		numBits++;
	}
}
