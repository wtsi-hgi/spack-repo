# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDjDatabaseUrl(PythonPackage):
	"""Use Database URLs in your Django Application."""
	
	homepage = "https://jazzband.co/projects/dj-database-url"
	pypi = "dj-database-url/dj_database_url-3.1.2-py3-none-any.whl" 

	version("0.1.2", sha256="6169f2c272326e3cced6999effb19013365ea73f6ed6c731efa4e346711d8969")
	version("0.1.3", sha256="222744896dcbe939aa940217c940a8a95981be13beb9af639a1da024be4f9411")
	version("0.1.4", sha256="14faa143247e267aefd807490e1e89e3ad9fac0a06c4aee3f9fe328849bd15cf")
	version("0.2.0", sha256="5edd253ccb407a0bd19e91c4c9bbe164632639767086b4a38f2d20e00010488b")
	version("0.2.1", sha256="f95c0b2e9e70cc246bd101720e1be492524ecf0dd5ea39241b51ef142faefecc")
	version("0.2.2", sha256="492a7294b85ad8ac1b13be0b7337f381d2d44c4da185f289ab7c26dd765ef6cb")
	version("0.3.0", sha256="ca01768fdecde134301f3170743226f60edff5c3935f12437378ebd911506353", expand=False, url="https://files.pythonhosted.org/packages/ef/b6/9283fcf61ced22bf90e7b4a84ba5b53d126b2c9b0dc9b667347698097026/dj_database_url-0.3.0-py2.py3-none-any.whl")
	version("0.4.0", sha256="858312abb7b330ea875733a65806a36ad04d7b8451c6ce8835118a2fa10d6870")
	version("0.4.1", sha256="7f4c78d2a090df8dfaf56d5d3ff7bbee17360436e4879558317e2314424864cd")
	version("0.4.2", sha256="e16d94c382ea0564c48038fa7fe8d9c890ef1ab1a8ec4cb48e732c124b9482fd", expand=False, url="https://files.pythonhosted.org/packages/91/84/50cbfabb91593cff18a37046986f7c2eb69224a694a52ae614711dfa11c6/dj_database_url-0.4.2-py2.py3-none-any.whl")
	version("0.5.0", sha256="851785365761ebe4994a921b433062309eb882fedd318e1b0fcecc607ed02da9", expand=False, url="https://files.pythonhosted.org/packages/d4/a6/4b8578c1848690d0c307c7c0596af2077536c9ef2a04d42b00fabaa7e49d/dj_database_url-0.5.0-py2.py3-none-any.whl")
	version("1.0.0", sha256="cd354a3b7a9136d78d64c17b2aec369e2ae5616fbca6bfbe435ef15bb372ce39", expand=False, url="https://files.pythonhosted.org/packages/4c/e7/c44c0088ed3d7a938c6509288c139e0c9eb45840c83c04cad74c19951910/dj_database_url-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="5f2f6b3f65786bac5d3b9e749bff1dcac83398d95778576909697f7b16aee6b9", expand=False, url="https://files.pythonhosted.org/packages/f3/55/c1af2b36b2337acf788744ca8941fc1877e4f248ae3021355855e40bf86a/dj_database_url-1.1.0-py3-none-any.whl")
	version("1.2.0", sha256="5c2993b91801c0f78a8b19e642b497b90831124cbade0c265900d4c1037b4730", expand=False, url="https://files.pythonhosted.org/packages/4f/62/e2786a98fda838f25ce86782810930b54eec2ad87d37950e80c3ce3538b8/dj_database_url-1.2.0-py3-none-any.whl")
	version("1.3.0", sha256="80a115bd7675c9fe14a900b2f8b5c8b1822b5a279b333bf9b2804de681656c7c", expand=False, url="https://files.pythonhosted.org/packages/20/8a/f41e4fe501bd276ac4d87c61c154be8862d640b1d41ff0503208d46b6c44/dj_database_url-1.3.0-py3-none-any.whl")
	version("2.0.0", sha256="9c9e5f7224f62635a787e9cc3c6762c9be2b19541a21e3c08fa573bd01609b4b", expand=False, url="https://files.pythonhosted.org/packages/6c/82/46c4560efd5117aa2a8365ed07f5267b297a1afa024411abe51e3a09fbd9/dj_database_url-2.0.0-py3-none-any.whl")
	version("2.1.0", sha256="04bc34b248d4c21aaa13e4ab419ae6575ef5f10f3df735ce7da97722caa356e0", expand=False, url="https://files.pythonhosted.org/packages/21/d2/b90366de4682c1472748b848292054e0960673f3c7d1a9d08fb227fad819/dj_database_url-2.1.0-py3-none-any.whl")
	version("2.2.0", sha256="3e792567b0aa9a4884860af05fe2aa4968071ad351e033b6db632f97ac6db9de", expand=False, url="https://files.pythonhosted.org/packages/6f/9a/13f173c716d07283661e821f7e1624d0904835151b4f099687455dbef81e/dj_database_url-2.2.0-py3-none-any.whl")
	version("2.3.0", sha256="bb0d414ba0ac5cd62773ec7f86f8cc378a9dbb00a80884c2fc08cc570452521e", expand=False, url="https://files.pythonhosted.org/packages/e5/91/641a4e5c8903ed59f6cbcce571003bba9c5d2f731759c31db0ba83bb0bdb/dj_database_url-2.3.0-py3-none-any.whl")
	version("3.0.0", sha256="cbb84b2e3f372460b1e43692bf9fdc0c32e78930ee101db470cba56105fca1e5", expand=False, url="https://files.pythonhosted.org/packages/e8/7b/d68df6365e442ae6370d6d970915329eae85bce5afb3602058d9ccc71700/dj_database_url-3.0.0-py3-none-any.whl")
	version("3.0.1", sha256="43950018e1eeea486bf11136384aec0fe55b29fe6fd8a44553231b85661d9383", expand=False, url="https://files.pythonhosted.org/packages/aa/5e/86a43c6fdaa41c12d58e4ff3ebbfd6b71a7cb0360a08614e3754ef2e9afb/dj_database_url-3.0.1-py3-none-any.whl")
	version("3.1.0", sha256="155a56fbbecbaaf1348ccd73bf29138b4c9988363ba08261a0f0145e392e638c", expand=False, url="https://files.pythonhosted.org/packages/68/1b/e84f7472ab0bdacc3fd09556eb4dd40d88246941d465cc103b36a8dabcd8/dj_database_url-3.1.0-py3-none-any.whl")
	version("3.1.1", sha256="245120e5df14008f0552b01c8a7d18127302ceea37f7686e55b8718daadf36f3", expand=False, url="https://files.pythonhosted.org/packages/49/4c/66cb2a0d09c0e311c08f3dcbccdbb3cb1e99533870286c99612ac844d563/dj_database_url-3.1.1-py3-none-any.whl")
	version("3.1.2", sha256="544e015fee3efa5127a1eb1cca465f4ace578265b3671fe61d0ed7dbafb5ec8a", expand=False, url="https://files.pythonhosted.org/packages/cf/a9/57c66006373381f1d3e5bd94216f1d371228a89f443d3030e010f73dd198/dj_database_url-3.1.2-py3-none-any.whl")

	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-django", type=("build", "run"))

# {'Django(>3.2)': ['1.0.0'], 'Django(>=3.2)': ['1.1.0', '1.2.0', '1.3.0', '2.0.0'], 'typing-extensions(>=3.10.0.0)': ['1.3.0', '2.0.0'], 'Django>=3.2': ['2.1.0', '2.2.0'], 'typing-extensions>=3.10.0.0': ['2.1.0', '2.2.0', '2.3.0'], 'Django>=4.2': ['2.3.0', '3.0.0', '3.0.1'], 'typing_extensions>=4.0.0': ['3.0.0'], 'django>=4.2': ['3.1.0', '3.1.1', '3.1.2']}