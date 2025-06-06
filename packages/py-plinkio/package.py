# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPlinkio(PythonPackage):
	"""A library for parsing plink genotype files"""
	
	homepage = "https://github.com/mfranberg/libplinkio"
	pypi = "plinkio/plinkio-0.9.8.tar.gz" 

	version("0.9.0", sha256="55650754557e0cfe0b967fdcbc4f02f51918c27200567eb6518c96d592ec9708")
	version("0.9.1", sha256="12a1cb84bfd6db8c1ad37abb91ac81742ca0fe471a22be01107cb8e5ed91ffa8")
	version("0.9.2", sha256="438bf27a1e3337add1bbdd0880e77f1673b9c8abbcca73d60890f97ff71c4a3c")
	version("0.9.4", sha256="52391269f354169f5b79e05184a7a38d009cc7033b989a2ce0e1fd21732a2e49")
	version("0.9.5", sha256="69b2877fa0253963de4784569af7a7af1316d9354f42ca41b588dd06f79ea7a1")
	version("0.9.6", sha256="a22a80bf0fb8bbd4d86601bc5eb5c57c3965b0c74d855d2030bf37eb29027b4b")
	version("0.9.7", sha256="578b5492c3005b7415e031ff209924998bb04bcf8c8680555f2d7aa8b544f79f")
	version("0.9.8", sha256="820cd57167ed28158f926ac4b2901b323f8593eb139bec000eeb3b895430011f")

	depends_on("py-setuptools", type=("build"))
