# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrso(RPackage):
	"""Cancer Rule Set Optimization ('crso')

	An algorithm for identifying candidate driver combinations in cancer. CRSO 
  is based on a theoretical model of cancer in which a cancer rule 
  is defined to be a collection of two or more events (i.e., alterations) that are minimally 
  sufficient to cause cancer. A cancer rule set is a set of cancer rules that collectively 
  are assumed to account for all of ways to cause cancer in the population. In CRSO every 
  event is designated explicitly as a passenger or driver within each patient. 
  Each event is associated with a patient-specific, event-specific passenger penalty, 
  reflecting how unlikely the event would have happened by chance, i.e., as a passenger.
  CRSO evaluates each rule set by assigning all samples to a rule in the rule set,
  or to the null rule, and then calculating the total statistical penalty from all
  unassigned event. CRSO uses a three phase procedure find the best rule set of 
  fixed size K for a range of Ks. A core rule set is then identified from among
  the best rule sets of size K as the rule set that best balances rule set size and 
  statistical penalty. 
  Users should consult the 'crso' vignette for an example walk through of a full CRSO run.
  The full description, of the CRSO algorithm is presented in: 
  Klein MI, Cannataro V, Townsend J, Stern DF and Zhao H. "Identifying combinations of cancer driver in individual patients." 
  BioRxiv 674234 [Preprint]. June 19, 2019. <doi:10.1101/674234>.
  Please cite this article if you use 'crso'.
	"""
	
	cran = "crso" 

	version("0.1.1", md5="241c0f4fd419b0c96c3b30d4bb40b643")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
