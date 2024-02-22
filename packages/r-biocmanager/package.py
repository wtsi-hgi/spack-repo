# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocmanager(RPackage):
	"""Access the Bioconductor Project Package Repository.

	A convenient tool to install and update Bioconductor packages."""

	cran = "BiocManager"

	version("1.30.22", md5="06077db0d01e97eedf0c96333a5506d7")

