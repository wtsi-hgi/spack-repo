# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransform(RPackage):
	"""Statistical Transformations

	Performs various statistical transformations; Box-Cox and Log (Box and Cox, 1964) <doi:10.1111/j.2517-6161.1964.tb00553.x>, Glog (Durbin et al., 2002) <doi:10.1093/bioinformatics/18.suppl_1.S105>, Neglog (Whittaker et al., 2005) <doi:10.1111/j.1467-9876.2005.00520.x>, Reciprocal (Tukey, 1957), Log Shift (Feng et al., 2016) <doi:10.1002/sta4.104>, Bickel-Docksum (Bickel and Doksum, 1981) <doi:10.1080/01621459.1981.10477649>, Yeo-Johnson (Yeo and Johnson, 2000)  <doi:10.1093/biomet/87.4.954>, Square Root (Medina et al., 2019), Manly (Manly, 1976) <doi:10.2307/2988129>, Modulus (John and Draper, 1980)  <doi:10.2307/2986305>, Dual (Yang, 2006) <doi:10.1016/j.econlet.2006.01.011>, Gpower (Kelmansky et al., 2013) <doi:10.1515/sagmb-2012-0030>. It also performs graphical approaches, assesses the success of the transformation via tests and plots.
	"""
	
	cran = "Transform" 

	version("1.0", md5="fddebf95a8f277739ba45fac5d1b0529")

	depends_on("r@3.2:", type=("build", "run"))
