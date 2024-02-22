# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHellorust(RPackage):
	"""Minimal Examples of Using Rust Code in R

	Template R package with minimal setup to use Rust code in R without
    hacks or frameworks. Includes basic examples of importing cargo dependencies,
    spawning threads and passing numbers or strings from Rust to R. Cargo crates
    are automatically 'vendored' in the R source package to support offline
    installation. The GitHub repository for this package has more details and also 
    explains how to set up CI. This project was first presented at 'Erum2018' to 
    showcase R-Rust integration <https://jeroen.github.io/erum2018/>; for a real
    world use-case, see the 'gifski' package on 'CRAN'.
	"""
	
	homepage = "https://github.com/r-rust/hellorust"
	cran = "hellorust" 

	version("1.2.0", md5="b9e66aafce80982def7853a4729ed97a")

	depends_on("rust", type=("build", "link", "run"))
