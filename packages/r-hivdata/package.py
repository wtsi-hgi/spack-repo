# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHivdata(RPackage):
	"""Six-Year Chronological Data of HIV and ART Cases in Pakistan

	We provide the monthly number of HIV and antiretroviral therapy (ART) cases of male, female, children and transgender as well as for the whole of Pakistan reported at various treatment centers in Pakistan from January 2016 to December 2021. Related works include: 
  a) Imran, M., Nasir, J. A., & Riaz, S. (2018). Regional pattern of HIV cases in Pakistan. Journal of Postgraduate Medical Institute, 32(1), 9-13. 
  <https://jpmi.org.pk/index.php/jpmi/article/view/2108>.  
	"""
	
	cran = "hivdata" 

	version("0.1.0", md5="3cc62ede90d580fcaec2a908f1ae1009")

	depends_on("r@4:", type=("build", "run"))
