# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPygsp(PythonPackage):
	"""Graph Signal Processing in Python"""
	
	homepage = "https://github.com/epfl-lts2/pygsp"
	pypi = "pygsp/PyGSP-0.5.1-py2.py3-none-any.whl" 

	version("0.2.0", sha256="4feb63ce58c32d192a42c6ecc899aa759efd7eed34a2db18471bb0b9e0709277", expand=False, url="https://files.pythonhosted.org/packages/ca/d3/3511615dfc964a9a07f763be29b8630d1c96a3631feae0f2c5ee86a7112c/PyGSP-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="5ce9ee6ac74fa6d77ed830f5bfc23e8d0e3d1d5c9b7c420029a38e17f5eb33fa", expand=False, url="https://files.pythonhosted.org/packages/55/ed/76316bd73da61980f136687988dab41912839c7eb5effaaa59d0601f5ddf/PyGSP-0.2.1-py2.py3-none-any.whl")
	version("0.3.0", sha256="8eca94b7bb3526f908ea65d946289b932f0394a320a9c2ae57016757c7847f4e", expand=False, url="https://files.pythonhosted.org/packages/fb/5e/5d45563e4f155e04e964f76e5979621f2f37f83f7d4fb3e60e5b66b2a9ad/PyGSP-0.3.3-py2.py3-none-any.whl")
	version("0.4.0", sha256="af2f810cb3ed0e365146aa6da211f36a94850baaffa75d3ed73295833f475972", expand=False, url="https://files.pythonhosted.org/packages/04/a7/618547cb775e778bd2b8a946e54b2faea3aa19f4e3ed20c64bf91f480a4c/PyGSP-0.4.0-py2.py3-none-any.whl")
	version("0.4.2", sha256="6886b7aa1230da3ba425d654eb8bd1c118727a5a6c834dc7eb4cfdce479a9dd0", expand=False, url="https://files.pythonhosted.org/packages/e6/c1/d0780497da02973a0541613e9b2d47e1db7ae15e3b7c35fda23b4be07104/PyGSP-0.4.1-py2.py3-none-any.whl")
	version("0.5.0", sha256="697368e5ae3f313a42f2ee28f648f2025e22660320e465dcf5c4c99fbf6bd138", expand=False, url="https://files.pythonhosted.org/packages/48/ea/402429ea743ee0e4ca6e65323f0b8d9d1e752d8182107dc401e31e6ffef0/PyGSP-0.5.0-py2.py3-none-any.whl")
	version("0.5.1", sha256="884765260256f143a92053c420797053fda0f4eba1573471526fb4e62a4c4cde", expand=False, url="https://files.pythonhosted.org/packages/d4/89/2f4aa73cccf12bec5179ac5d52a68b508120c838b7e5d456f5ea0c8beade/PyGSP-0.5.1-py2.py3-none-any.whl")

