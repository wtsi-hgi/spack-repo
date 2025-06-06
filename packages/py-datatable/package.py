# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDatatable(PythonPackage):
	"""Python library for fast multi-threaded data manipulation and munging."""
	
	homepage = "https://github.com/h2oai/datatable"
	pypi = "datatable/datatable-1.1.0.tar.gz" 

	version("0.10.1", sha256="3ce5257c0c4afa96e2b14ca47a0aaf73add195b11de48f4adda50b5ede927436")
	version("0.11.0", sha256="19c602711e00f72e9ae296d8fa742d46da037c2d3a2d254bdf68f817a8da76bb")
	version("0.11.1", sha256="3c3a7d3bee3c463a36fe77c5d4747278a741c23fc6c6e2dba110deec200502ba")
	version("0.3.1", sha256="f37eda31d581fe266684a0adeea581f379615751f1b7ef1270b65fb065315fa9")
	version("0.3.2", sha256="ec3a57521b8856ba19aae1cd83322220257b34a8dc9a89a66c0a2d4c477fd58e")
	version("0.4.0", sha256="2f400223c427a7f61812b28120315e94408119a049479aef213f0d4161ef5822")
	version("0.5.0", sha256="699f750ee9896db71ef8a58758bae757c8995d473579f8685a82279ebc6ee9c7")
	version("0.6.0", sha256="7861146df1cb087208180bec058614f5b2dc427a0fcf5eb535340d39b9f9fae7")
	version("0.7.0", sha256="97b8a942c542a7d11eb634f1955e3b32906425ed2a6b7c23baa4568949f8fcd8")
	version("0.8.0", sha256="53e657e07c87b6802633eff5547897bbe977989c17d09c79db9365e77e401fe9")
	version("0.9.0", sha256="ae986a4fed9f2671f66f269300dfbb23d84b4e6b7c9f62b53252799bea941cea")
	version("1.0.0", sha256="59a00a4a928f9b06f881d4f7b5e9025c559c4f65facf903a5d08e6e94d84c31e")
	version("1.1.0", sha256="8a9f6953ef6b02ede3d7c490f17d5c18c9b1bf2d58dd5451a8cac40ed887d775")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.6:", type=("build", "run"))
