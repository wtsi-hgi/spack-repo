# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPims(PythonPackage):
	"""Python Image Sequence"""
	
	homepage = "https://github.com/soft-matter/pims"
	pypi = "pims/pims-0.7rc1.tar.gz" 

	version("0.2", sha256="fb3c66447537401e4bc89b882a90419fbd1ebe13f0cc329fc387baa5783db1a1")
	version("0.2.1", sha256="05dfde1e73077c0846a6903ad6ce2b42e3e5f8431634490531d99f146440406c")
	version("0.2.2", sha256="15e7f77370d149afd871fa9f2da620334ae8e1ecad31c5093bab1a92402a2345")
	version("0.2.2rc1", sha256="d0aa2c4429d7e8dcddd694dd9b02d17dcf4fc2ae8b91528c360d5478ad143989")
	version("0.2.2rc2", sha256="0a8b8a17eff61bd42455ff8a827a88cac745b699c78306a79eeb07e868558004")
	version("0.3.0", sha256="3dbe23ece6645c871ef275d705eaa4da4e3ad588264b8fc711e7fb0030994f95")
	version("0.3.1", sha256="759a85ae43db6f53605326651f0c84fb218ccc0a60a420f0f5cac5ed2961c4fd")
	version("0.3.2", sha256="cad956f455eee535329411981345c257fa1d7f63ad0ae5bd7c45102be010b19c")
	version("0.3.2rc1", sha256="ea4265070b45df707f4971f215db5216829fcdbb34e372587d3d582925f0370a")
	version("0.3.2rc2", sha256="8caab9376aee0809ecf36bf9c7fea4db7cfa76b7e7d2d1343ed51f46aec70147")
	version("0.3.3", sha256="6b777cee3c4c3449aca1237144ec4ce06f958a6e8a9292beea56cee1397e08c6")
	version("0.3.3rc1", sha256="bfeee07d9613cf62f722108570f719ee48044ee24beec52265d104a3b1f82ab6")
	version("0.4", sha256="d3269b157f678184bda1a4278f76db9b9e64e9b8d252201308dce7ae0d270789")
	version("0.4.1", sha256="e79f3c0c6acaff6d48041723cb11f057c18c7ffb00f8a0095e365db4e60d4350", expand=False, url="https://files.pythonhosted.org/packages/00/08/bbf9f5465c92ea6577bc5824fea21d2583e24e94fe10cc853587ffcacda0/PIMS-0.4.1-py3-none-any.whl")
	version("0.4rc1", sha256="7b10d201dcb09edeb124b49ca54e4431fbde4111ea064f82a3e79b09a18572aa")
	version("0.5", sha256="a02cdcbb153e2792042fb0bae7df4f30878bbba1f2d176114a87ee0dc18715a0")
	version("0.5rc1", sha256="2aa2f6143878bdca555960ca673a2ff27014260aab97a93b3ac3cbda58ac702a")
	version("0.6.0", sha256="64d37e436e1f9c6ace5fe568ce8d401b20828702ec4cab649a3532da73759f60", expand=False, url="https://files.pythonhosted.org/packages/ef/9c/17bef9691e31d9f7964342cdbdce21154fea15288dfb9536513cac09cc52/PIMS-0.6.0-py3-none-any.whl")
	version("0.6.1", sha256="e2b704461d4ea9bce8b6a22ca35836fe67d6d34537736b405341ae5547194f3b")
	version("0.6.1rc1", sha256="52c8490295b373ffb78fb0e55177f9a8622b47cc3887e60a4d8843c2c3d8b1d9")
	version("0.7", sha256="55907a4c301256086d2aa4e34a5361b9109f24e375c2071e1117b9491e82946b")
	version("0.7rc1", sha256="2aa2f734b8d7587c841c9ec29f846fb7431ec22c2d73cbb3ef27fe0bf5fd0405")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))

# {'numpy(>=1.7)': ['0.4.1'], 'six(>=1.8)': ['0.4.1'], 'slicerator(>=0.9.7)': ['0.4.1'], 'imageio': ['0.6.0'], 'numpy(>=1.19)': ['0.6.0'], 'slicerator(>=0.9.8)': ['0.6.0']}