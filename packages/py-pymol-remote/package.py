# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPymolRemote(PythonPackage):
	"""Send data to and from pymol from a remote server (e.g. a cluster running deep learning workflows)"""
	
	homepage = "https://github.com/Croydon-Brixton/pymol-remote"
	pypi = "pymol-remote/pymol_remote-1.1.0-py3-none-any.whl" 

	version("0.0.4", sha256="4ceb1cb6c99a4f549d74d5a8185954b7c7ca76e3dace164015cedc51f7532d66", expand=False, url="https://files.pythonhosted.org/packages/e2/fb/42ee71745fabeb01335ee1c5ae44cab1102afd6ee428994f30050baa5c3d/pymol_remote-0.0.4-py3-none-any.whl")
	version("0.0.5", sha256="d9efa062aeb802e10de935d14cc11a0d557613d74c40e73c8479680baeb3e9b2", expand=False, url="https://files.pythonhosted.org/packages/83/55/f97fb96b48c334e247641382e66e18876a78fd0667a62a1ee761c309180e/pymol_remote-0.0.5-py3-none-any.whl")
	version("0.1.0", sha256="dc7426a1485d75f635fdac36ef8500d3c497ee7f7429c105cbf9caf04bf91fb6", expand=False, url="https://files.pythonhosted.org/packages/2b/88/02a7aacd27f7fc59cc3d9d8b3c65900b123d97e58a3919f28c1143fe07e8/pymol_remote-0.1.0-py3-none-any.whl")
	version("1.0.0", sha256="6516347ba10c028a71962c1d4b30ff23bb9d0f378a736d53fe2c49953b62f8ec", expand=False, url="https://files.pythonhosted.org/packages/10/17/cf6e0eedcec3f5de2a0487804c0c21fe2666b103ba60e1be066010bd7e79/pymol_remote-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="32170b896bcf21e6c7d4716ff1f98d358bc80376c9e175aa5e8b86ba245813fc", expand=False, url="https://files.pythonhosted.org/packages/48/16/9a5bb7ef3bcc5b5a0e708cec0bd08069b87223e77c429b6c0b294b3bae49/pymol_remote-1.1.0-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
