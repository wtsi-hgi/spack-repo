# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioassayr(RPackage):
	"""Cross-target analysis of small molecule bioactivity

	bioassayR is a computational tool that enables simultaneous analysis of thousands of bioassay experiments performed over a diverse set of compounds and biological targets. Unique features include support for large-scale cross-target analyses of both public and custom bioassays, generation of high throughput screening fingerprints (HTSFPs), and an optional preloaded database that provides access to a substantial portion of publicly available bioactivity data.
	"""
	
	homepage = "https://github.com/girke-lab/bioassayR"
	bioc = "bioassayR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bioassayR_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bioassayR/bioassayR_1.40.0.tar.gz"]

	version("1.40.0", md5="94ac7a2ff2a9de7b65d8ebd864513a31")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
