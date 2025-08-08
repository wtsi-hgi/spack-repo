# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiff(RPackage):
	"""Read and write TIFF images.

	This package provides an easy and simple way to read, write and display
	bitmap images stored in the TIFF format. It can read and write both files
	and in-memory raw vectors."""

	cran = "tiff"
	version("0.1-6", sha256="623bd9c16a426df7e6056738c5d91da86ea9b49df375eea6b5127e4e458dc4fb")
	version("0.1-5", sha256="9514e6a9926fcddc29ce1dd12b1072ad8265900373f738de687ef4a1f9124e2b")
	version("0.1-12", md5="2e24ff9e6afffa8243c6d1a5356aa374")
	version("0.1-11", sha256="b8c3ea15114d972f8140541c7b01f5ce2e5322af1f63c1a083aaf766fd3eec75")
	version("0.1-10", sha256="535154e89e85e14fe697469d2c59826a44c7937e7eca2eaca1aee6b0fe320afe")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))

	def setup_build_environment(self, env):
		"""Ensure package configure checks can find R headers.

		R 4.4 adds `-include R_ext/Memory.h` to default flags, which requires
		explicit inclusion of R's headers during configure-time tests.
		"""
		r_include = join_path(self.spec["r"].prefix, "rlib", "R", "include")
		env.append_flags("CPPFLAGS", f"-I{r_include}")
		env.append_flags("PKG_CPPFLAGS", f"-I{r_include}")
