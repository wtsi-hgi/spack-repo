# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasiliskUtils(RPackage):
	"""Basilisk Installation Utilities.

	Implements utilities for installation of the basilisk package, primarily
	for creation of the underlying Conda instance. This allows us to avoid
	re-writing the same R code in both the configure script (for centrally
	administered R installations) and in the lazy installation mechanism (for
	distributed package binaries). It is highly unlikely that developers - or,
	heaven forbid, end-users! - will need to interact with this package
	directly; they should be using the basilisk package instead."""

	bioc = "basilisk.utils"

	license("GPL-3.0-only")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/basilisk.utils_1.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/basilisk.utils/basilisk.utils_1.14.1.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.1", sha256="474007e52f5a18e9e76c7e0fad7121cba2a77aed02c649e98fd5cc994182a4a6")
	version("1.12.0", commit="8314f9a72ecc0f20b180431aec93647320de8c2c")

	depends_on("r-dir-expiry", type=("build", "run"))
