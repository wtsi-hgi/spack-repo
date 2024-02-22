# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsetools(RPackage):
	"""Ion Selective Electrodes Analysis Methods

	Characterisation and calibration of single or multiple Ion Selective Electrodes (ISEs); 
    activity estimation of experimental samples. Implements methods described in:
	Dillingham, P.W., Radu, T., Diamond, D., Radu, A. and McGraw, C.M. (2012) <doi:10.1002/elan.201100510>,  
	Dillingham, P.W., Alsaedi, B.S.O. and McGraw, C.M. (2017) <doi:10.1109/ICSENS.2017.8233898>,
	Dillingham, P.W., Alsaedi, B.S.O., Radu, A., and McGraw, C.M. (2019) <doi:10.3390/s19204544>, and
	Dillingham, P.W., Alsaedi, B.S.O., Granados-Focil, S., Radu, A., and McGraw, C.M. (2020)  <doi:10.1021/acssensors.9b02133>.
	"""
	
	cran = "ISEtools" 

	version("3.2.0", md5="19c70d708e4b1ee207f1b7f5106bef5d")

	depends_on("r-coda", type=("build", "run"))
