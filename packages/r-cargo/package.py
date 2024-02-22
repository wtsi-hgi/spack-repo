# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCargo(RPackage):
	"""Develop R Packages using Rust

	A framework is provided to develop R packages using 'Rust' <https://www.rust-lang.org/> with
 minimal overhead, and more wrappers are easily added. Help is provided to use 'Cargo' <https://doc.rust-lang.org/cargo/> in a manner
 consistent with CRAN policies. 'Rust' code can also be embedded directly in an R script. The package is not official, affiliated with,
 nor endorsed by the Rust project.
	"""
	
	homepage = "https://github.com/dbdahl/cargo-framework"
	cran = "cargo" 

	version("0.4.9", md5="63f5a276207e29d8194ce51a6f5b100a")

	depends_on("r@4.2:", type=("build", "run"))
