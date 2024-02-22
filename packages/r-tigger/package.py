# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigger(RPackage):
	"""Infers Novel Immunoglobulin Alleles from Sequencing Data

	Infers the V genotype of an individual from immunoglobulin (Ig)
    repertoire sequencing data (AIRR-Seq, Rep-Seq). Includes detection of 
    any novel alleles. This information is then used to correct existing V 
    allele calls from among the sample sequences.
    Citations:
    Gadala-Maria, et al (2015) <doi:10.1073/pnas.1417683112>,
    Gadala-Maria, et al (2019) <doi:10.3389/fimmu.2019.00129>.
	"""
	
	homepage = "http://tigger.readthedocs.io"
	cran = "tigger" 

	version("1.1.0", md5="080334af65c18d484d3e1454f629326f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-alakazam@1.3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
