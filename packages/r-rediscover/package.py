# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRediscover(RPackage):
	"""Identify Mutually Exclusive Mutations

	An optimized method for identifying mutually 
    exclusive genomic events.  Its main contribution is a
    statistical analysis based on the Poisson-Binomial 
    distribution that takes into account that some samples
    are more mutated than others. See [Canisius, Sander, John WM Martens,
    and  Lodewyk FA Wessels. (2016)  "A novel independence test for
    somatic alterations in cancer shows that 
    biology drives mutual exclusivity but chance explains
    most co-occurrence." Genome biology 17.1 : 1-17. <doi:10.1186/s13059-016-1114-x>].
    The mutations matrices are sparse matrices. The method developed takes 
    advantage of the advantages of this type of matrix to save 
    time and computing resources.
	"""
	
	cran = "Rediscover" 

	version("0.3.2", md5="13cb52983d50a32c4c92ad4e71bdd264")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-poissonbinomial", type=("build", "run"))
	depends_on("r-shiftconvolvepoibin", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
