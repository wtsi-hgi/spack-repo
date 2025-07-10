# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHspeccdf(RPackage):
	"""hspeccdf

	A package containing an environment representing the HGU133Plus2_Hs_Hspec.cdf file.
	"""
	
	bioc = "hspeccdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hspeccdf_0.99.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hspeccdf/hspeccdf_0.99.1.tar.gz"]

	version("0.99.1", sha256="dc110b7a22826dd1ae93ce71ca305e72a89580359784480f8ba294777fa25f1d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

