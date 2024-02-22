# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcv(RPackage):
	"""Enhanced Coefficient of Variation and IDR Extensions for
Reproducibility Assessment

	
    Reproducibility assessment is essential in extracting reliable scientific 
    insights from high-throughput experiments.  While  the  Irreproducibility 
    Discovery   Rate   (IDR)   method  has  been  instrumental  in  assessing 
    reproducibility,  its  standard implementation is constrained to handling
    only two  replicates. Package 'eCV' introduces an enhanced Coefficient of
    Variation  (eCV)  metric  to assess the likelihood of omic features being 
    reproducible. Additionally, it offers alternatives  to  the  Irreproducible
    Discovery  Rate  (IDR)  calculations for multi-replicate experiments. 
    These  tools  are  valuable for analyzing high-throughput data in genomics
    and  other  omics  fields. The methods implemented in 'eCV' are  described 
    in Gonzalez-Reymundez et al., (2023) <doi:10.1101/2023.12.18.572208>.
	"""
	
	homepage = "https://github.com/eclipsebio/eCV"
	cran = "eCV" 

	version("0.0.2", md5="5e6a76f50c30d8873913ec2823f5dfdc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-idr@1.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-future@1.4:", type=("build", "run"))
	depends_on("r-future-apply@1.9:", type=("build", "run"))
