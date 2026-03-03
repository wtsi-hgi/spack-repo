from spack.package import *


class PyPod5(PythonPackage):
	"""Oxford Nanopore Technologies POD5 File Format Python API and Tools"""

	homepage = "https://github.com/nanoporetech/pod5-file-format"
	pypi = "pod5/pod5-0.3.28-py3-none-any.whl"

	version("0.3.28", sha256="721149a97c5c3396ff5014d37d67eb113d0089e70d1a0cdb40752c1aaa503f52", expand=False)

	depends_on("py-setuptools", type="build")
	depends_on("python@3.9:3.9", type=("build", "run"))
	depends_on("py-lib-pod5", type=("build", "run"))
	depends_on("py-iso8601", type=("build", "run"))
	depends_on("py-more-itertools", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pyarrow", type=("build", "run"))
	depends_on("py-pytz", type=("build", "run"))
	depends_on("py-packaging", type=("build", "run"))
	depends_on("py-polars", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))
	depends_on("py-vbz-h5py-plugin", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))


