# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMdtraj(PythonPackage):
	"""MDTraj: A modern, open library for the analysis of molecular dynamics trajectories"""
	
	homepage = "http://mdtraj.org"
	pypi = "mdtraj/mdtraj-1.9.9.tar.gz" 

	version("0.3", sha256="4cbd8bbeebacd0fae186244b817edd5dfd7546426fbe7bc2a80002644baa9b8a")
	version("0.3.1", sha256="86d8b14ea7e8757475f32e346a05e7d8bb0e374d6c7b89a7d7fa9ba7f76acd09")
	version("0.4.0", sha256="8eb89b88c3e900e0594ebbaff55c07a59959411a69c7e436933b899e81d7d3e4")
	version("0.4.1", sha256="0b0e6c28aa596e442ea3763c7ffdcc6f714152c330b9b799b088f5c4bd8bd553")
	version("0.4.3", sha256="183b42cb33c97ffc8321eea42a8f9bf1dc8daf70fcd77ed1a2f010ceb1aa6ddc")
	version("0.5.0", sha256="7f675810a15632557b6974402b52c2a317f65e4aefb21cc4fb9e5f59c2a6a035")
	version("0.5.1", sha256="258a81b7b500493e36ea590f7222ae06df4782a6d5de4d04a3569a831a98584b")
	version("0.6.0", sha256="7ebfc1a1249d973f203f6e141211cdb1c5fa8a43f7058f19304d0269378edccc")
	version("0.6.1", sha256="49bb8956ce3bc8f43dfb7fdf0897217a2e170cb7180311951c323af62aee3388")
	version("0.7.0", sha256="b45210e1d7eabdb9ff30338bcbbbc6d7624720ddd7d76c9ceb88f2baaaa5289f")
	version("0.8.0", sha256="d255f9f0509205109aa08a853fdb004cac9e8075b5ba370d17903519ff7c0f39")
	version("0.9.0", sha256="dcc380dbcea821f50bceb6f3492d46122a6b15336a12cb50cd49d31d9700e687")
	version("1.0.0", sha256="8aa8e04038453b3201d906e1ecb01cb4261f0e9230d72e62786255f68e09d86d")
	version("1.1.0", sha256="fc842a7adf741036580c82afae83dab547578bd6dd59d3e93956d8a0fd5e07ad")
	version("1.10.0", sha256="7d518b5a53b498f52686567e0191e9ee41a725b3296a8dbcac24fe824ed4af8f")
	version("1.10.0rc1", sha256="aa17c098cee7e6d5a1cd89324f74820e04417dc94eb37018bfdc7cfbac2bdb48")
	version("1.10.0rc2", sha256="86ff2073025743cc841e3a0f457e3931ea40f6359d8ce5600d9d46baa83e2885")
	version("1.10.1", sha256="2e427d007194a64cf2ac92e1e10572d975ba914ab63e315b747738d71cf148da")
	version("1.10.2", sha256="8108bd42792b653f96c9352956f1100ccebbe21b0fe598b05a7a85c39704136f")
	version("1.10.3", sha256="d14a35009263725b784c436a8ac63fb6ceeb2bb366a526715dac6590d21025e5")
	version("1.2.0", sha256="b6e930608c366b86ff6523485264788caf12b7f5c8be369bbc98ee31d569551e")
	version("1.3.0", sha256="7be7a99823c08ef93f01483815774c0ac9aefd8c3790d0f9069fe6685bf3a45b")
	version("1.4.0", sha256="6337fe3cc50c9ad1c745019e84175dd3c56b108b7f3000e1296549969c6916de")
	version("1.4.1", sha256="b58cb4ff9cc191871b06d71768128584753a8136d09cd8ff5445da333bc283c9")
	version("1.4.2", sha256="dc1c31b956ad5e88590048abaaaa33bad58887262e94e2921c070d9e6d5fd5df")
	version("1.5.0", sha256="e56dcf4b7be97c007692b6c6758f8fc8b84811e666de1c3836631e697dab9394")
	version("1.5.1", sha256="d97591eebf1e9ae04c2b2e144340a959ed359fe33037c647b174f017bab482c3")
	version("1.6.0", sha256="9d281e43cbc7133615dc0b81e63f64e79e39e3d25098103798301f3c06383c0b")
	version("1.6.1", sha256="bca98c6339d04b36934b37857eae9f42fb667e1745d4d7dc29ebfd4e3c653365")
	version("1.7.2", sha256="3158176cd2c21d2abdff5b2cbd9cac323f337b831123d5201bbb7d3fbe69e714")
	version("1.8.0", sha256="867325cb206dca4a605de4877e17e5e1983f2e778a6ef64594bd4250142561a8")
	version("1.9.1", sha256="ca1ae07c5f5ce59940a48388ac9b098f8e22743b5f3ed3f46d5e3d1317b06282")
	version("1.9.2", sha256="cdd926f19c007955f0f768d36d696f3e77b4c8030289a2b40eb97a91cebacd0f")
	version("1.9.3", sha256="5d95e045b1dd093a26bf6fea9895c3c6b52955d8f7fceee867a519ccf29640b3")
	version("1.9.4", sha256="d5d28be24dd5f38e8b272c3a445a6cdbffc374b30e891c5535f65bb20f7e8b24")
	version("1.9.5-py36", sha256="c02a9a589acc98dd3cc4db9b0cb21725f5e2cb9484c14cc4fa032a4663c7a1e9", expand=False, url="https://files.pythonhosted.org/packages/1b/77/3ac1597812fc28964662587d405f85986206192623b434f7d0fa1b4a6a5b/mdtraj-1.9.5-cp36-cp36m-manylinux1_x86_64.whl")
	version("1.9.5-py37", sha256="8816f9a91826e46a413fd1a5ffd663b4076cf4c3b8930bb2046814d1438a88ee", expand=False, url="https://files.pythonhosted.org/packages/af/da/271e93bb98bc93ccac17bc1f31f814be4f9e7024ac19bf31af892a462030/mdtraj-1.9.5-cp37-cp37m-manylinux1_x86_64.whl")
	version("1.9.5-py38", sha256="84bb3ced0ff61c4b3b38a36d71837599f50c8723c5d9e555dced51d0d09e10a1", expand=False, url="https://files.pythonhosted.org/packages/3b/fd/4ffba665d0b0346072f61d0e8ef7ab281202db445d99136c717c89169a97/mdtraj-1.9.5-cp38-cp38-manylinux1_x86_64.whl")
	version("1.9.5-py39", sha256="7eae1adc6aa876396c9797d80db3f71da831601fb1739da731e1de9ca8ac96ab", expand=False, url="https://files.pythonhosted.org/packages/68/53/2f666107565f4735abd859b6af6867353eb08d0e9728d90fb0abc12d578e/mdtraj-1.9.5-cp39-cp39-manylinux1_x86_64.whl")
	version("1.9.6-py36", sha256="8d437742ec45ff619c7a50afacf16f3a791d604cd0be74b5b74d90b0dc3f577a", expand=False, url="https://files.pythonhosted.org/packages/fe/a7/2a1392fe56ddd22a9cf5dcff7d684bdd7ce146d5c32839080dd8de7122dd/mdtraj-1.9.6-cp36-cp36m-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("1.9.6-py37", sha256="49f4251f83a7fdea4a8122369ef47f213bb1c1cfc38b91177e98985484fb63bf", expand=False, url="https://files.pythonhosted.org/packages/ce/ee/2015ff88cacb7c75b5e1cf6a57e8a089549b0e76bcd9474a08845f7ef12f/mdtraj-1.9.6-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("1.9.6-py38", sha256="84bf863729d435df0dd1f86c3023cbe85b8940b102f9d6ef6ce00dcb9130883c", expand=False, url="https://files.pythonhosted.org/packages/c0/61/2fb002b9b2ab90567eb1a837ed510152ddadd5b8358ac800b591e37675e0/mdtraj-1.9.6-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("1.9.6-py39", sha256="44fcc435df4057126c123585e36a8a4563e24588ad438c916751e2e01501e2ff", expand=False, url="https://files.pythonhosted.org/packages/09/49/85dc22a3c28108dfd0bce8a4268ae3937167b18fac531a0d801505cad7d9/mdtraj-1.9.6-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("1.9.7", sha256="8a3309d2ef6ddb1023dcf48300d5df9b190469b63f69af9d55490bc4799d3757")
	version("1.9.8", sha256="a886c497b0e1868c07d95da29a754ed41b3413000a0f21c616b7b9201ba862cb")
	version("1.9.9", sha256="1b03f7ac753af5ca07cf874842689c8d49e791ee1242510875581df6100ca15e")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-versioneer+toml", type="build")
	depends_on("py-cython@0.29:", type="build")
	depends_on("py-pyparsing", type=("build", "run"))
	depends_on("py-netcdf4", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-packaging", type=("build", "run"))
	depends_on("python@3.6", when="@1.9.5-py36", type=("build", "run"))
	depends_on("python@3.7", when="@1.9.5-py37", type=("build", "run"))
	depends_on("python@3.8", when="@1.9.5-py38", type=("build", "run"))
	depends_on("python@3.9", when="@1.9.5-py39", type=("build", "run"))
	depends_on("python@3.6", when="@1.9.6-py36", type=("build", "run"))
	depends_on("python@3.7", when="@1.9.6-py37", type=("build", "run"))
	depends_on("python@3.8", when="@1.9.6-py38", type=("build", "run"))
	depends_on("python@3.9", when="@1.9.6-py39", type=("build", "run"))

# {'numpy(>=1.6)': ['1.9.5-py36', '1.9.5-py37', '1.9.5-py38', '1.9.5-py39', '1.9.6-py36', '1.9.6-py37', '1.9.6-py38', '1.9.6-py39'], 'scipy': ['1.9.5-py36', '1.9.5-py37', '1.9.5-py38', '1.9.5-py39', '1.9.6-py36', '1.9.6-py37', '1.9.6-py38', '1.9.6-py39'], 'astunparse': ['1.9.5-py36', '1.9.5-py37', '1.9.5-py38', '1.9.5-py39', '1.9.6-py36', '1.9.6-py37', '1.9.6-py38', '1.9.6-py39'], 'pyparsing': ['1.9.5-py36', '1.9.5-py37', '1.9.5-py38', '1.9.5-py39', '1.9.6-py36', '1.9.6-py37', '1.9.6-py38', '1.9.6-py39']}