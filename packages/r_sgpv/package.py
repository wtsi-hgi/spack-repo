# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgpv(RPackage):
	"""Calculate Second-Generation p-Values and Associated Measures

	Computation of second-generation p-values as described in Blume et al. (2018) <doi:10.1371/journal.pone.0188299> and Blume et al. (2019) <doi:10.1080/00031305.2018.1537893>. There are additional functions which provide power and type I error calculations, create graphs (particularly suited for large-scale inference usage), and a function to estimate false discovery rates based on second-generation p-value inference. 
	"""
	
	cran = "sgpv" 

	version("1.1.0", md5="3614ee88de1c7547652e3a26695b0c6c")

	depends_on("r@3.3.3:", type=("build", "run"))
