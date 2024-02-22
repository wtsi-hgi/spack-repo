# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGopro(RPackage):
	"""Find the most characteristic gene ontology terms for groups of human genes

	Find the most characteristic gene ontology terms for groups of human genes. This package was created as a part of the thesis which was developed under the auspices of MI^2 Group (http://mi2.mini.pw.edu.pl/, https://github.com/geneticsMiNIng).
	"""
	
	homepage = "https://github.com/mi2-warsaw/GOpro"
	bioc = "GOpro" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GOpro_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GOpro/GOpro_1.28.0.tar.gz"]

	version("1.28.0", md5="c92dbcab08a7cdac3ee8ee6c28c6dc78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
