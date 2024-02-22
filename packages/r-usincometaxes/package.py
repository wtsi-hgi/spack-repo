# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsincometaxes(RPackage):
	"""Calculate Federal and State Income Taxes in the United States

	Calculates federal and state income taxes in the United States. It acts as a wrapper 
    to the NBER's TAXSIM 35 (<http://taxsim.nber.org/taxsim35/>) tax simulator. TAXSIM 35 conducts 
    the calculations, while 'usincometaxes' prepares the data for TAXSIM 35, sends the data to 
    TAXSIM 35's server or communicates with the Web Assembly file, retrieves the data, and places it 
    into a data frame. All without the user worrying about this process.
	"""
	
	homepage = "https://github.com/shanejorr/usincometaxes"
	cran = "usincometaxes" 

	version("0.7.1", md5="3f976887af0d513b1a5a5c4923455b7b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
