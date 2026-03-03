# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiverdist(RPackage):
	"""River Network Distance Computation and Applications

	Reads river network shape files and computes network distances.
    Also included are a variety of computation and graphical tools designed 
    for fisheries telemetry research, such as minimum home range, kernel density 
    estimation, and clustering analysis using empirical k-functions with 
    a bootstrap envelope.  Tools are also provided for editing the river 
    networks, meaning there is no reliance on external software.
	"""
	
	homepage = "https://cran.r-project.org/package=riverdist"
	cran = "riverdist" 

	version("0.16.3", md5="d504c75c63a56eda376a57c226057672")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
