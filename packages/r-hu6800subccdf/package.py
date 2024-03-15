# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu6800subccdf(RPackage):
	"""hu6800subccdf

	A package containing an environment representing the Hu6800subC.CDF file.
	"""
	
	bioc = "hu6800subccdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu6800subccdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu6800subccdf/hu6800subccdf_2.18.0.tar.gz"]

	version("2.18.0", md5="020fe3a6bdf44efbde15432b968433e8")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation