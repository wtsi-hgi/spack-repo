# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTypeinfo(RPackage):
	"""Optional Type Specification Prototype

	A prototype for a mechanism for specifying the types of parameters and the return value for an R function. This is meta-information that can be used to generate stubs for servers and various interfaces to these functions. Additionally, the arguments in a call to a typed function can be validated using the type specifications. We allow types to be specified as either i) by class name using either inheritance - is(x, className), or strict instance of - class(x) %in% className, or ii) a dynamic test given as an R expression which is evaluated at run-time. More precise information and interesting tests can be done via ii), but it is harder to use this information as meta-data as it requires more effort to interpret it and it is of course run-time information. It is typically more meaningful.
	"""
	
	bioc = "TypeInfo" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TypeInfo_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TypeInfo/TypeInfo_1.68.0.tar.gz"]

	version("1.74.0", tag="RELEASE_3_21")
	version("1.68.0", sha256="fa05cc4a02beb5c76294af5b9d311513aef63b06d6300cbda940c579224c49e4")

