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

	version("1.46.0", commit="5088ff6158d8889561b2c8a26f5553011e05ff56")
	version("1.40.0", commit="b838e6617001a7fcde6ad80d010f5881070ba2e0")

	depends_on("r-gwastools", type=("build", "run"))

