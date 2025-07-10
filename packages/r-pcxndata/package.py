# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcxndata(RPackage):
	"""Correlation coefficients and p values between pre-defined pathway/gene sets

	PCxN database contains correlation coefficients and p values between pre-defined gene sets within MSigDB H hallmark gene sets, MSigDB C2 CP (Canonical pathways), MSigDB C5 GO BP gene sets and Pathprint respectively, as well as adjusted pathway correlations to account for the shared genes between pathway pairs.
	"""
	
	bioc = "pcxnData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/pcxnData_2.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/pcxnData/pcxnData_2.24.0.tar.gz"]

	version("2.24.0", sha256="124c63d4ed955a4d161351041adf5a4e9e8f23db78c04494159d5982627c1856")

	depends_on("r@3.4:", type=("build", "run"))

