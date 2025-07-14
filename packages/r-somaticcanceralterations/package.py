# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomaticcanceralterations(RPackage):
	"""Somatic Cancer Alterations

	Collection of somatic cancer alteration datasets
	"""
	
	bioc = "SomaticCancerAlterations" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SomaticCancerAlterations_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SomaticCancerAlterations/SomaticCancerAlterations_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="2898d77e34ddef6f58bda8fb210a7c9c9fe5aab7cf8348c7d2b6016381b00b90")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

