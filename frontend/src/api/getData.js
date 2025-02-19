PORT = 8000;
BASE_URL = `http://localhost:${PORT}`;

export const getApiStatus = async function (success, fail) {
  await axios({
    method: "get",
    url: BASE_URL
  })
    .then(success)
    .catch(fail);
};

export const getMenuWeek = async function (success, fail) {
  await axios({
    method: "get",
    url: `${BASE_URL}/menu/week`
  })
    .then(success)
    .catch(fail);
};

export const getMenuDay = async function (day, success, fail) {
  await axios({
    method: "get",
    url: `${BASE_URL}/menu/day/${day}`
  })
    .then(success)
    .catch(fail);
};
