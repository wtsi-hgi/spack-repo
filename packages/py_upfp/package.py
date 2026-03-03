# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyUpfp(PythonPackage):
	"""UPFP, a package to parse UniProt FASTA files."""
	
	homepage = "https://github.com/drugilsberg/uniprot_fasta_parser"
	pypi = "upfp/upfp-0.0.5.tar.gz" 

	version("0.0.3", sha256="c49a6f7043db1c85c15f48a890aa068a04288fcf4098e0b45b3dab5f4174b66c", expand=False, url="https://files.pythonhosted.org/packages/9c/53/095e775308b4fd607ad64a085850a9ac2d8556d9d83cc0417c14b43011bd/upfp-0.0.3-py3-none-any.whl")
	version("0.0.4", sha256="df6cbd31e771f0f61e3f4b45a0bd3b7253c74adf146d061ebb7b52bf70110b53", expand=False, url="https://files.pythonhosted.org/packages/0f/27/d77a0daa2d95a5313498734ad582ff4d928373a4bbd6e39ffdb70d127d00/upfp-0.0.4-py3-none-any.whl")
	version("0.0.5", sha256="af91c282429e558128e7d65bb18572105820a4fbc57fd4b964a954a2e3315f84")

	depends_on("py-setuptools", type="build")
# {'pandas(>=0.24.2)': ['0.0.3', '0.0.4']}