# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlexdatr(RPackage):
	"""Kootenay Lake Exploitation Study Data

	Six relational 'tibbles' from the Kootenay Lake Large Trout Exploitation study.
  The study which ran from 2008 to 2014 caught, tagged and released large Rainbow Trout and Bull Trout
  in Kootenay Lake by boat angling. 
  The fish were tagged with internal acoustic tags and/or high reward external tags
  and subsequently detected by an acoustic receiver array as well as reported by anglers.
  The data are analysed by Thorley and Andrusak (1994) <doi:10.7717/peerj.2874>
  to estimate the natural and fishing mortality of both species.
	"""
	
	homepage = "https://github.com/poissonconsulting/klexdatr"
	cran = "klexdatr" 

	version("0.1.2", md5="b37bfc4475fd70d00278efc70210ac74")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
