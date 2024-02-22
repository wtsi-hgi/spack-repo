# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasdata(RPackage):
	"""Data used in the examples and vignettes of the GWASTools package

	Selected Affymetrix and Illlumina SNP data for HapMap subjects.  Data provided by the Center for Inherited Disease Research at Johns Hopkins University and the Broad Institute of MIT and Harvard University.
	"""
	
	bioc = "GWASdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/GWASdata_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/GWASdata/GWASdata_1.40.0.tar.gz"]

	version("1.40.0", md5="57fec70f980b9e476f0c59d397797815")

	depends_on("r-gwastools", type=("build", "run"))

	# experiment