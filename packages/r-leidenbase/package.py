# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeidenbase(RPackage):
	"""R and C/C++ Wrappers to Run the Leiden find_partition() Function

	An R to C/C++ interface that runs the Leiden community
    detection algorithm to find a basic partition (). It runs the
    equivalent of the 'leidenalg' find_partition() function, which is
    given in the 'leidenalg' distribution file
    'leiden/src/functions.py'. This package includes the
    required source code files from the official 'leidenalg'
    distribution and functions from the R 'igraph'
    package.  The 'leidenalg' distribution is available from
    <https://github.com/vtraag/leidenalg/>
    and the R 'igraph' package is available from
    <https://igraph.org/r/>.
    The Leiden algorithm is described in the article by
    Traag et al. (2019) <doi:10.1038/s41598-019-41695-z>.
    Leidenbase includes code from the packages:
       igraph version 0.9.8 with license GPL (>= 2),
       leidenalg version 0.8.10 with license GPL 3.
	"""
	
	homepage = "https://github.com/cole-trapnell-lab/leidenbase"
	cran = "leidenbase" 

	version("0.1.27", md5="410d97dc1222fbfc207d4f7588afaaaf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph@0.9:", type=("build", "run"))
