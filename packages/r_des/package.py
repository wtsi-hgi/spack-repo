# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDes(RPackage):
	"""Discrete Event Simulation

	Discrete event simulation (DES) involves modeling of systems
   having discrete, i.e. abrupt, state changes. For instance, when a job
   arrives to a queue, the queue length abruptly increases by 1.  This
   package is an R implementation of the event-oriented approach to DES;
   see the tutorial in Matloff (2008) 
   <http://heather.cs.ucdavis.edu/~matloff/156/PLN/DESimIntro.pdf>.
	"""
	
	cran = "DES" 

	version("1.0.0", md5="b61a17d9696d1f2fc9bc346f9309cc83")

