# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyqtwebengine(PythonPackage):
	"""Python bindings for the Qt WebEngine framework"""
	
	homepage = "https://www.riverbankcomputing.com/software/pyqtwebengine/"
	pypi = "PyQtWebEngine/PyQtWebEngine-5.15.7.tar.gz" 

	version("5.12", sha256="62b4ef3afb3ab54d667e46237380ad6cdc2acc31b59cecb45b3bdce1a464c7cd", expand=False, url="https://files.pythonhosted.org/packages/49/e3/73c258c655c0785ec22af5367ee0be0a63a79ef026f68eca5300ec842282/PyQtWebEngine-5.12-5.12.1-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl")
	version("5.12.1", sha256="37b7a245b0ed4ed6cdd032db2ebb02cb0239582dc72dad54c30df0c428c26aa2", expand=False, url="https://files.pythonhosted.org/packages/90/c9/bde6c215e9b08f149e5e8936b512dabfe0c3c8893c1397d2c53965a3dc4f/PyQtWebEngine-5.12.1-5.12.10-cp35.cp36.cp37.cp38.cp39-abi3-manylinux1_x86_64.whl")
	version("5.13.0", sha256="dd4952f6671e10fcb572274e964f324778e75b6da5586c30f4b99a2b44857e95", expand=False, url="https://files.pythonhosted.org/packages/a5/e8/1ed5d3af4549aaba3d60578cd35d1cb1b3adf74a7164cd7b93036caf41d6/PyQtWebEngine-5.13.0-5.13.0-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl")
	version("5.13.1", sha256="814156fccf11b0b95dc1a3e7b8b774c584678c0ea97ed03aa36a37f7a52913f0", expand=False, url="https://files.pythonhosted.org/packages/6f/f7/4d0c6b5fcb93a2e0067f2618638d4c46aa5286e96a9236c40269e6c5c5ee/PyQtWebEngine-5.13.1-5.13.1-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl")
	version("5.13.2", sha256="1266b24490d5425665109a7d0de85daadb5a4b23f37ec61c0664af37c7a140a8", expand=False, url="https://files.pythonhosted.org/packages/8c/62/5463c863eae4309816fd3be7a7eb947e176b9126fb14cad4b4e9dc1bc514/PyQtWebEngine-5.13.2-5.13.2-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl")
	version("5.14.0", sha256="e11595051f8bfbfa49175d899b2c8c2eea3a3deac4141edf4db68c3555221c92")
	version("5.15.0", sha256="670812688e40bf75f70ddf01eadd897d231300318d3856b275bf8e7e0085bf75")
	version("5.15.1", sha256="f0ca7915ee206ba5d703168c6ca40b0aad62c67360328fae4af5359cdbcee439")
	version("5.15.2", sha256="4d72fea774071ce6f76e341a3d2c5d595886c9906a9b9493239c841cce54a634")
	version("5.15.3", sha256="0badc56e6c9ee2b7b4baa87511737d2a7f1de5a45f52b1da8f4965fc17dcf0b6")
	version("5.15.4", sha256="cedc28f54165f4b8067652145aec7f732a17eadf6736835852868cf76119cc19")
	version("5.15.5", sha256="782aeee6bc8699bc029fe5c169a045c2bc9533d781cf3f5e9fb424b85a204e68", expand=False, url="https://files.pythonhosted.org/packages/a1/45/667e82a0f584be10d785213b04c8ce01ae4d2f63cd23ab6307312c69be89/PyQtWebEngine-5.15.5-cp36-abi3-manylinux1_x86_64.whl")
	version("5.15.6", sha256="67110bc9d5b7e633dcc242b8228cc54b1532abc039fdf534b383ac40a60b7ba3", expand=False, url="https://files.pythonhosted.org/packages/cd/90/fcc59d99ed597ac3d1aa465f8c7711cb33e02cc867940db6c62dcdaa2689/PyQtWebEngine-5.15.6-cp37-abi3-manylinux1_x86_64.whl")

	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-pyqt5@5.15.4:", type=("build", "run"))
	depends_on("py-pyqtwebengine-qt5", type=("build", "run"))
	depends_on("py-pyqt5-sip", type=("build", "link", "run"))
	depends_on("py-pyqt-builder", type=("build", "link", "run"))

# {'PyQt5(>=5.12)': ['5.12', '5.12.1'], 'PyQt5(>=5.13)': ['5.13.0', '5.13.1', '5.13.2'], 'PyQt5-sip(>=12.8,<13)': ['5.15.5'], 'PyQtWebEngine-Qt5(>=5.15.2)': ['5.15.5'], 'PyQt5(>=5.15.4)': ['5.15.5', '5.15.6'], 'PyQt5-sip(>=12.11,<13)': ['5.15.6'], 'PyQtWebEngine-Qt5(>=5.15.0)': ['5.15.6']}
