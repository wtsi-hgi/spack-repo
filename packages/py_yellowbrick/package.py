# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyYellowbrick(PythonPackage):
	"""A suite of visual analysis and diagnostic tools for machine learning."""
	
	homepage = "http://scikit-yb.org/"
	pypi = "yellowbrick/yellowbrick-1.5-py3-none-any.whl" 

	version("0.1-py2", sha256="fc2ca7bfd8b53c3f2bc4617ff30ae8fcb539bfb5a585efaab0bf03227cbfd13d", expand=False, url="https://files.pythonhosted.org/packages/2a/27/0ff26cadaa272649a0c65ffb9a7dadfb46f85ca525b1abff1d0aee1edba8/yellowbrick-0.1-py2-none-any.whl")
	version("0.3.1", sha256="e34e1c207bbf976370c881ad8bf9dd09b912544f767e0606fd357d75d448031a", expand=False, url="https://files.pythonhosted.org/packages/59/2a/c20f580454c7d7863219d2ef22adc5d5cf4df552e227b844582a5f5c035d/yellowbrick-0.3.1-py2.py3-none-any.whl")
	version("0.3.2", sha256="1ebedba36615b25d36e5e0412d7fa06a053feb128600d882e4292ada53cee534", expand=False, url="https://files.pythonhosted.org/packages/71/73/e5ba5c8ec9d7448eeabf78fa2e6dd94ed8ada12bd8816904725b642aba82/yellowbrick-0.3.2-py2.py3-none-any.whl")
	version("0.3.3", sha256="cb793a9efd61152a963cf23c5b8eb4abed437ab308ad37ef76c9781da74ee7c6", expand=False, url="https://files.pythonhosted.org/packages/54/ac/fb068972b0c998577b26ef83c8ffbbbd3fb4c7ddf112b1426521dbaf631d/yellowbrick-0.3.3-py2.py3-none-any.whl")
	version("0.3a1", sha256="99f44d3050f02e09bf78e3e90135fdae3af69801b42c05fc6a666bb5472cb314", expand=False, url="https://files.pythonhosted.org/packages/89/3f/5bf5c6fd1a08e73caa49f07f02b01510c5e8564039ec57ae43d03a77b7d5/yellowbrick-0.3a1-py3-none-any.whl")
	version("0.4", sha256="cf3e860deac36802a3e6e950ba9ccd43110035b48ad557a7f12f6a7aef0c4a36", expand=False, url="https://files.pythonhosted.org/packages/e5/0e/4d167ba83aa2467ded08e53eb77f93b5abf2638c73c827a7b7c4fbd66fce/yellowbrick-0.4-py2.py3-none-any.whl")
	version("0.4.1", sha256="3cb3b8b8de674df1f0c352ef6d90469975b5121818b97d27eccb7d05dc9df76c", expand=False, url="https://files.pythonhosted.org/packages/f3/d9/0cf903d81b1cbb785dde7ee4e90410bbec5350f522dcbb83138154e7e19e/yellowbrick-0.4.1-py2.py3-none-any.whl")
	version("0.4.2", sha256="54b56eee4c4da13a99e62aa0bd928c5de8288a2b527ef52fd0b9bf3b403b343e", expand=False, url="https://files.pythonhosted.org/packages/dc/d6/211662e4815f1470fc0997d3e9f94f1e312086a9ccc152f5d338d0f9fb50/yellowbrick-0.4.2-py2.py3-none-any.whl")
	version("0.5", sha256="898f5e2b397b5a2d9424ce952f315c4eb44e789b9fde37ee0c5328c37d015104", expand=False, url="https://files.pythonhosted.org/packages/25/d7/73de84d138fb32ceedbdbe064c9939b5e09a599cc574ea1b32ecc01226f2/yellowbrick-0.5-py2.py3-none-any.whl")
	version("0.6", sha256="312c6c2934d79707dd95bf09f2b884d30bc4ba4130be3f102e01e6d10ff95581", expand=False, url="https://files.pythonhosted.org/packages/10/a0/d13295d0c4f9130a1881831d3bd00a255e7c54e1fa512ca6599037a49b9b/yellowbrick-0.6-py2.py3-none-any.whl")
	version("0.7", sha256="4c7e45dd9c90caa2aaae4be647469e897eca49b1d69c257a6b082b369a8e02ab", expand=False, url="https://files.pythonhosted.org/packages/16/c7/e78d507a55cdde7e05050b59a073f5bf8f927240375f6aa870c591fcf707/yellowbrick-0.7-py2.py3-none-any.whl")
	version("0.8", sha256="744f074d78bb7855dbf25418b09db82dc0bf027013c318fc8f6e20932b85d584", expand=False, url="https://files.pythonhosted.org/packages/ca/64/ffa3ae377d0841595335f9ae402ecd777d7a275746c7389feb68c1386110/yellowbrick-0.8-py2.py3-none-any.whl")
	version("0.9", sha256="6099d38e35364fa1f14db6d43592d75706c14b36bee12e106cc732f4a5dced1b", expand=False, url="https://files.pythonhosted.org/packages/f0/b3/fffa077157c38e729eb033fdd0ad57fbe92db1aac303c69b283ce10deb9b/yellowbrick-0.9-py2.py3-none-any.whl")
	version("0.9.1", sha256="0c089613e6b13e277a030a74380c14d63d56b2567e006a7d26ec4ae7490386f1", expand=False, url="https://files.pythonhosted.org/packages/d8/e8/125204ea84a7424a3237556e8dfaec9fee21f2e3d5b3695eb9ce355bf668/yellowbrick-0.9.1-py2.py3-none-any.whl")
	version("1.0", sha256="005c44d78248d779ff5e0353daf122ea00c2c15a1b39e78ebf62f26e0e902a83", expand=False, url="https://files.pythonhosted.org/packages/f4/71/c63c404f718fdb2f69ff1c16d4e6c92384483c3616929977fff4cb082593/yellowbrick-1.0-py2.py3-none-any.whl")
	version("1.0.1", sha256="36b2028629415f3c7a90a4feddaed59ba2ed4052a1e3a0f1ef93d5735e779224", expand=False, url="https://files.pythonhosted.org/packages/d1/cf/6d6ab47c0759d246262f9bdb53e89be3814bf1774bc51fffff995f5859f9/yellowbrick-1.0.1-py3-none-any.whl")
	version("1.0.post1", sha256="33d85861c1df5296836e10744f14d8ccf307b62b7f3ea51100db63a85a9b5960", expand=False, url="https://files.pythonhosted.org/packages/44/4c/7c04104a1e89a7a1d7d557d91219a47b4bf148f3f0e6f185dce24fb73b9b/yellowbrick-1.0.post1-py3-none-any.whl")
	version("1.1", sha256="a753daf750c80903fdb7ae3ad2313a578971e851693e8ef7565d722cd2b6813b", expand=False, url="https://files.pythonhosted.org/packages/13/95/a14e4fdfb8b1c8753bbe74a626e910a98219ef9c87c6763585bbd30d84cf/yellowbrick-1.1-py3-none-any.whl")
	version("1.2-py2", sha256="4bd29df714cae0e09de0d7e070db169410437d2bc110e10a1c1376d6fcc074f4", expand=False, url="https://files.pythonhosted.org/packages/84/50/7e9a94a0ddc8788fee8d2049143e896193c8ba8328f702cb3e86219d0a7f/yellowbrick-1.2-py2-none-any.whl")
	version("1.2", sha256="5268168df9dcb6cbcd66a1061689295ad39eb30372bee7b7cc0728e61cc715f0", expand=False, url="https://files.pythonhosted.org/packages/1f/ad/ae6744ddb9c7053916bed95430152b9a41b7d410e16a1cc7cd744a611d90/yellowbrick-1.2-py3-none-any.whl")
	version("1.2.1", sha256="ac89c8fffe151fc17e20f4825da57e68c02356d6f1151b66370f8114555ab1e6", expand=False, url="https://files.pythonhosted.org/packages/b1/bb/57fd86c319a43666fe447bb1bc5af66fb0eb89dc4efc305a7544d50f52d6/yellowbrick-1.2.1-py3-none-any.whl")
	version("1.3", sha256="d8e3576eafc4ef12c9e6a4a6e70fceda78fd0d7c21011332e03534a0f44ed646", expand=False, url="https://files.pythonhosted.org/packages/d4/64/5e1cf10fb2ace980b71c992d1b84c807d8e69e9eddb389b35825b640ea48/yellowbrick-1.3-py3-none-any.whl")
	version("1.3.post1", sha256="69b70196af1793d130d062326ef630a8630903d4f7499e010f662b0e450d1adb", expand=False, url="https://files.pythonhosted.org/packages/3a/15/58feb940b6a2f52d3335cccf9e5d00704ec5ba62782da83f7e2abeca5e4b/yellowbrick-1.3.post1-py3-none-any.whl")
	version("1.4", sha256="16cc4af0474272b9ce103e3d061ff4b74edacf281f206cd7c483418357c5831b", expand=False, url="https://files.pythonhosted.org/packages/a4/dc/fb17b2aa792d67353456899c36e8e2a4dfe284e9ed3124f85fc3879cea2a/yellowbrick-1.4-py3-none-any.whl")
	version("1.5", sha256="4bb2895cecf94a0e736398bbac6c5d72032ba3ff2273f49df660b14ef419305d", expand=False, url="https://files.pythonhosted.org/packages/06/35/c7d44bb541c06bc41b3239b27af79ea0ecc7dbb156ee1335576f99c58b91/yellowbrick-1.5-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.4:", type=("build", "run"))
	depends_on("py-cycler", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("python@2", when="@0.1-py2", type=("build", "run"))
	depends_on("python@2", when="@1.2-py2", type=("build", "run"))

# {'matplotlib(==1.5.1)': ['0.1-py2'], 'numpy(==1.11.0)': ['0.1-py2'], 'scikit-learn(==0.17.1)': ['0.1-py2'], 'cycler(>=0.10.0)': ['0.3.1', '0.3.2', '0.3.3', '0.3a1', '0.4', '0.4.1', '0.4.2', '0.5', '0.6', '0.7', '0.8', '0.9', '0.9.1', '1.0', '1.0.1', '1.0.post1', '1.1', '1.2-py2', '1.2', '1.2.1', '1.3', '1.3.post1', '1.4', '1.5'], 'matplotlib(>=1.5.1)': ['0.3.1', '0.3.2', '0.3.3', '0.3a1', '0.4', '0.4.1', '0.4.2', '0.5', '0.6', '0.7', '0.8'], 'numpy(>=1.11.0)': ['0.3.1', '0.3.2', '0.3.3', '0.3a1', '0.4', '0.4.1', '0.4.2', '0.5'], 'scikit-learn(>=0.17.1)': ['0.3.1', '0.3.2', '0.3.3', '0.3a1', '0.4'], 'scipy(>=0.17.1)': ['0.3.1', '0.3.2', '0.3.3', '0.3a1', '0.4'], 'scikit-learn(>=0.18)': ['0.4.1', '0.4.2', '0.5'], 'scipy(>=0.18)': ['0.4.1', '0.4.2', '0.5'], 'scipy(>=0.19)': ['0.6', '0.7', '0.8'], 'scikit-learn(>=0.19)': ['0.6', '0.7', '0.8'], 'numpy(>=1.13.0)': ['0.6', '0.7', '0.8', '0.9', '0.9.1', '1.0', '1.0.1', '1.0.post1', '1.1', '1.2-py2', '1.2', '1.2.1'], 'matplotlib(<3.0,>=1.5.1)': ['0.9'], 'scipy(>=1.0.0)': ['0.9', '0.9.1', '1.0', '1.0.1', '1.0.post1', '1.1', '1.2-py2', '1.2', '1.3', '1.3.post1', '1.4', '1.5'], 'scikit-learn(>=0.20)': ['0.9', '0.9.1', '1.0', '1.0.1', '1.0.post1', '1.1', '1.2-py2', '1.2', '1.3', '1.3.post1'], 'matplotlib(!=3.0.0,>=1.5.1)': ['0.9.1'], 'matplotlib(!=3.0.0,>=2.0.2)': ['1.0', '1.0.1', '1.0.post1', '1.1', '1.2-py2', '1.2', '1.2.1', '1.3', '1.3.post1', '1.4', '1.5'], 'scipy(<1.6,>=1.0.0)': ['1.2.1'], 'scikit-learn(<0.24,>=0.20)': ['1.2.1'], 'numpy(<1.20,>=1.16.0)': ['1.3', '1.3.post1'], 'scikit-learn(>=1.0.0)': ['1.4', '1.5'], 'numpy(>=1.16.0)': ['1.4', '1.5']}