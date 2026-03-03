# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJson64(RPackage):
	"""A 'Base64' Encode/Decode Package with Support for JSON
Output/Input and UTF-8

	Encode/Decode 'base64', with support for JSON format, using two functions: j_encode() and j_decode().    'Base64' is a group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation, used when there is a need to encode binary data that needs to be stored and transferred over media that are designed to deal with textual data, ensuring that the data will remain intact and without modification during transport. <https://developer.mozilla.org/en-US/docs/Web/API/WindowBase64/Base64_encoding_and_decoding>    On the other side, JSON (JavaScript Object Notation) is a lightweight data-interchange format. Easy to read, write, parse and generate. It is based on a subset of the JavaScript Programming Language. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. JSON structure is built around name:value pairs and ordered list of values. <https://www.json.org>    The first function, j_encode(), let you transform a data.frame or list to a 'base64' encoded JSON (or JSON string).    The j_decode() function takes a 'base64' string (could be an encoded JSON) and transform it to a data.frame (or list, depending of the JSON structure).
	"""
	
	cran = "json64" 

	version("0.1.3", md5="7dac6f527082478285dbcf47fa30a843", url="https://cran.r-project.org/src/contrib/json64_0.1.3.tar.gz")

	depends_on("r-jsonlite", type=("build", "run"))
