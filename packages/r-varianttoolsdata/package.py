# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarianttoolsdata(RPackage):
	"""Data for the VariantTools tutorial

	Data from the sequencing of a 50/50 mixture of HapMap trio samples NA12878 (CEU) and NA19240 (YRI), subset to the TP53 region.
	"""
	
	bioc = "VariantToolsData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/VariantToolsData_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/VariantToolsData/VariantToolsData_1.26.0.tar.gz"]

    version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="d5adcce32790706f8bca6948c92c9d77ad3efd4a65f91e2169af835bc5e5484a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-variantannotation@1.7.35:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

